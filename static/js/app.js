// =====================================================================
// APP.JS — SWEET CUPCAKE GOURMET
// Interações leves e acessíveis no cliente (Padrão MVC - Camada View)
// =====================================================================

document.addEventListener("DOMContentLoaded", () => {
  // Auto-dismiss em alertas flash após 5 segundos
  const alerts = document.querySelectorAll(".alert-box");
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.style.transition = "opacity 0.4s ease";
      alert.style.opacity = "0";
      setTimeout(() => alert.remove(), 400);
    }, 5000);
  });
});
