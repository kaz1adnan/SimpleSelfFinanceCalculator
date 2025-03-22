# SimpleSelfFinanceCalculator
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Financial Calculator Program</title>
</head>
<body>
    <h1>Financial Calculator Program</h1>

    <h2>What the Program Does:</h2>

    <ol>
        <li>
            <strong>User Input Selection:</strong>
            <ul>
                <li>Asks the user to choose between two options:</li>
                <li><code>'returns'</code> – Calculate future wealth over a set number of years.</li>
                <li><code>'freedom'</code> – Determine how many years it will take to reach financial freedom.</li>
            </ul>
        </li>

        <li>
            <strong>Data Collection:</strong>
            <ul>
                <li>Prompts the user to enter:</li>
                <li><strong>Current Wealth:</strong> Initial amount of money you have.</li>
                <li><strong>Rate of Return (%):</strong> Annual percentage return on investments.</li>
                <li><strong>Monthly Savings:</strong> Amount saved every month.</li>
                <li>If the user selects <code>'freedom'</code>, it also asks for <strong>Target Wealth:</strong> The amount needed to be financially free.</li>
            </ul>
        </li>

        <li>
            <strong>Option 1: 'returns' – Wealth Calculation Over Time:</strong>
            <ul>
                <li>Simulates the growth of <strong>total wealth</strong> for a specified number of years.</li>
                <li>Each year, it adds:</li>
                <ul>
                    <li><strong>Interest:</strong> Based on the rate of return.</li>
                    <li><strong>Annual Savings:</strong> Monthly savings × 12.</li>
                </ul>
                <li>Prints the <strong>total wealth</strong> at the end of each year.</li>
            </ul>
        </li>

        <li>
            <strong>Option 2: 'freedom' – Years Until Financial Freedom:</strong>
            <ul>
                <li>Repeats the calculation annually until <strong>total savings</strong> exceed the <strong>target wealth</strong>.</li>
                <li>Displays how many <strong>years</strong> it will take to reach the target and prints a motivational message.</li>
            </ul>
        </li>

        <li>
            <strong>Error Handling:</strong>
            <ul>
                <li>If the user enters invalid input (e.g., non-numeric values), the program displays an error message and exits.</li>
            </ul>
        </li>

        <li>
            <strong>Program Flow:</strong>
            <ul>
                <li>Continues running calculations until it meets the conditions or the user provides incorrect input.</li>
            </ul>
        </li>
    </ol>

</body>
</html>
