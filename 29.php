$id = $_GET['id'];$query = "SELECT * FROM products WHERE id = " . $id;$result = $db->query($query);