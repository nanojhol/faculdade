// =====================================================================
// APP.JS — SWEET CUPCAKE GOURMET
// Interações acessíveis: Adicionar ao Carrinho assíncrono, Toasts,
// e Auto-atualização de status a cada 10 segundos no Acompanhamento.
// =====================================================================

document.addEventListener("DOMContentLoaded", () => {

  // 1. Auto-dismiss em alertas flash tradicionais
  const alerts = document.querySelectorAll(".alert-box");
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.transition = "opacity 0.4s ease";
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 400);
    }, 6000);
  });

  // 2. Interceptação assíncrona do "Adicionar ao Carrinho" (Vitrine)
  const formsAdd = document.querySelectorAll(".form-add-carrinho");
  formsAdd.forEach(form => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const btn = form.querySelector(".btn-add-carrinho");
      const btnText = btn.querySelector(".btn-text") || btn;
      const originalText = btnText.innerHTML;
      const produtoNome = form.dataset.nome || "Cupcake";

      const formData = new FormData(form);

      try {
        btn.disabled = true;
        btnText.innerHTML = "Adicionando...";

        const response = await fetch(form.action, {
          method: "POST",
          body: formData,
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "Accept": "application/json"
          }
        });

        if (response.ok) {
          const data = await response.json();

          // Atualiza o contador de itens no cabeçalho imediatamente
          const contadorNav = document.getElementById("carrinho-contador");
          if (contadorNav && data.carrinho_qtd !== undefined) {
            contadorNav.textContent = data.carrinho_qtd;
            contadorNav.style.transform = "scale(1.3)";
            setTimeout(() => contadorNav.style.transform = "scale(1)", 300);
          }

          // Transição de feedback no botão
          btn.classList.add("btn-sucesso-adicionado");
          btnText.innerHTML = "✔ Adicionado!";

          // Notificação toast flutuante
          showToast(`🧁 ${data.message || `${produtoNome} adicionado ao carrinho!`}`, "sucesso");

          setTimeout(() => {
            btn.classList.remove("btn-sucesso-adicionado");
            btnText.innerHTML = originalText;
            btn.disabled = false;
          }, 1800);

        } else {
          showToast("Não foi possível adicionar o produto.", "erro");
          btnText.innerHTML = originalText;
          btn.disabled = false;
        }
      } catch (err) {
        console.error("Erro ao adicionar ao carrinho:", err);
        showToast("Erro de conexão ao adicionar.", "erro");
        btnText.innerHTML = originalText;
        btn.disabled = false;
      }
    });
  });

  // 3. Atualização automática em tempo real a cada 10 segundos no Acompanhamento
  const trackerBox = document.getElementById("tracker-box");
  if (trackerBox) {
    const pedidoId = trackerBox.dataset.pedidoId;
    let statusAtual = trackerBox.dataset.statusAtual;

    console.log(`[Rastreio] Monitorando Pedido #${pedidoId} a cada 10s. Status inicial: ${statusAtual}`);

    setInterval(async () => {
      try {
        const resp = await fetch(`/api/pedido/${pedidoId}/status`, {
          headers: { "Accept": "application/json" }
        });

        if (resp.ok) {
          const dados = await resp.json();
          if (dados.status_entrega && dados.status_entrega !== statusAtual) {
            console.log(`[Rastreio] Mudança detectada: ${statusAtual} -> ${dados.status_entrega}`);
            statusAtual = dados.status_entrega;
            trackerBox.dataset.statusAtual = statusAtual;

            // Atualiza linha do tempo visual
            atualizarTimelineVisual(statusAtual);

            // Atualiza o texto do alerta descritivo
            atualizarAlertaDescritivo(statusAtual);

            // Atualiza badge lateral se existir
            const badgeSidebar = document.getElementById(`badge-sidebar-${pedidoId}`);
            if (badgeSidebar) {
              badgeSidebar.textContent = formatarStatus(statusAtual);
              badgeSidebar.style.background = getBadgeBg(statusAtual);
              badgeSidebar.style.color = getBadgeColor(statusAtual);
            }

            // Exibe notificação ao cliente
            showToast(`🛵 Pedido #${pedidoId} atualizado: ${formatarStatus(statusAtual)}!`, "sucesso");
          }
        }
      } catch (e) {
        console.warn("[Rastreio] Falha na consulta de status de 10s:", e);
      }
    }, 10000);
  }

});

// Helper de Toasts Flutuantes
function showToast(mensagem, tipo = "sucesso") {
  let container = document.getElementById("toast-container");
  if (!container) {
    container = document.createElement("div");
    container.id = "toast-container";
    container.className = "toast-container";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");
  toast.className = "toast";
  toast.innerHTML = mensagem;

  container.appendChild(toast);

  setTimeout(() => {
    toast.classList.add("toast-fadeout");
    setTimeout(() => toast.remove(), 400);
  }, 4000);
}

// Helpers para Linha do Tempo e Status
function atualizarTimelineVisual(status) {
  const s1 = document.getElementById("step-1");
  const s2 = document.getElementById("step-2");
  const s3 = document.getElementById("step-3");
  const s4 = document.getElementById("step-4");
  if (!s1 || !s2 || !s3 || !s4) return;

  [s1, s2, s3, s4].forEach(s => {
    s.classList.remove("active", "completed");
  });

  if (status === "RECEBIDO") {
    s1.classList.add("completed");
  } else if (status === "PREPARANDO") {
    s1.classList.add("completed");
    s2.classList.add("active");
  } else if (status === "EM_ROTA") {
    s1.classList.add("completed");
    s2.classList.add("completed");
    s3.classList.add("active");
  } else if (status === "ENTREGUE") {
    s1.classList.add("completed");
    s2.classList.add("completed");
    s3.classList.add("completed");
    s4.classList.add("completed");
  }
}

function atualizarAlertaDescritivo(status) {
  const alertBox = document.getElementById("status-alert-desc");
  if (!alertBox) return;

  if (status === "RECEBIDO") {
    alertBox.innerHTML = "📥 <strong>Pedido recebido:</strong> Registrado na cozinha e aguardando o início da montagem.";
  } else if (status === "PREPARANDO") {
    alertBox.innerHTML = "🧁 <strong>Na cozinha:</strong> Seus cupcakes estão sendo confeitados artesanalmente com carinho.";
  } else if (status === "EM_ROTA") {
    alertBox.innerHTML = "🛵 <strong>A caminho:</strong> O entregador já saiu da confeitaria e está a caminho do seu endereço!";
  } else if (status === "ENTREGUE") {
    alertBox.innerHTML = "✨ <strong>Entregue com sucesso:</strong> Esperamos que saboreie cada mordida! Bom apetite.";
  }
}

function formatarStatus(status) {
  const map = {
    'RECEBIDO': 'Recebido',
    'PREPARANDO': 'Em Preparo',
    'EM_ROTA': 'Em Rota',
    'ENTREGUE': 'Entregue'
  };
  return map[status] || status;
}

function getBadgeBg(status) {
  const map = {
    'RECEBIDO': '#e3f2fd',
    'PREPARANDO': '#fff3e0',
    'EM_ROTA': '#f3e5f5',
    'ENTREGUE': '#e8f5e9'
  };
  return map[status] || '#f0f0f0';
}

function getBadgeColor(status) {
  const map = {
    'RECEBIDO': '#1565c0',
    'PREPARANDO': '#e65100',
    'EM_ROTA': '#7b1fa2',
    'ENTREGUE': '#2e7d32'
  };
  return map[status] || '#333';
}
