window.addEventListener("DOMContentLoaded", async () => {
  const ctx = document.getElementById("expenseChart").getContext("2d");
  const response = await fetch("/chart-data");
  const data = await response.json();

  const chart = new Chart(ctx, {
    type: "pie",
    data: {
      labels: Object.keys(data),
      datasets: [
        {
          label: "Expenses by Category",
          data: Object.values(data),
          backgroundColor: [
            "#2ecc71",
            "#3498db",
            "#e74c3c",
            "#f1c40f",
            "#9b59b6",
            "#e67e22",
          ],
        },
      ],
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "bottom",
        },
      },
    },
  });
});
