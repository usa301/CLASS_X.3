document.addEventListener("DOMContentLoaded", function() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#dataKelas tbody');
            data.forEach(item => {
                const row = document.createElement('tr');
                row.innerHTML = `<td>${item.nama}</td><td>${item.kelas}</td><td>${item.nilai}</td>`;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
