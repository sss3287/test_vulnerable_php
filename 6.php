$userInput = $_POST['input'];$output = shell_exec("ping " . $userInput);