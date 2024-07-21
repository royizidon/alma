// script.js
document.getElementById('queryForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const query = document.getElementById('userQuery').value;
    const responseDiv = document.getElementById('response');
    
    const response = await fetch('http://localhost:5000/api/query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
    });
    
    const data = await response.json();
    if (data.pdf) {
        const pdfData = 'data:application/pdf;base64,' + data.pdf;
        const link = document.createElement('a');
        link.href = pdfData;
        link.download = 'map.pdf';
        link.click();
        responseDiv.innerHTML = '<p>PDF downloaded successfully.</p>';
    } else {
        responseDiv.innerHTML = '<p>No PDF generated.</p>';
    }
});
               