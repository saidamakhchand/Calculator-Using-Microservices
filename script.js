function appendToResult(value) {
    document.getElementById('result').value += value;
}

function clearResult() {
    document.getElementById('result').value = '';
}

async function getResult() {
    const expression = document.getElementById('result').value;
    try {
        const response = await fetch(`http://127.0.0.1:8000/calculate?expression=${encodeURIComponent(expression)}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.json();
        document.getElementById('result').value = data.result !== undefined ? data.result : data.error;
    } catch (error) {
        document.getElementById('result').value = "Error: " + error.message;
    }
}

function calculateResult(operator) {
    const currentValue = document.getElementById('result').value;
    // إضافة العامل للنتيجة الحالية
    if (currentValue !== '') {
        document.getElementById('result').value += ` ${operator} `;
    }
}
