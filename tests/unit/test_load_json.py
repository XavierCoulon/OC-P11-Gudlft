from ... import server


class TestLoadClass:

	def test_load_json(self):
		assert server.load_json("tests/json_dataset") == [
			{"field1": "Club 1", "field2": "club1@gmail.com", "field3": "40"},
			{"field1": "Club 2", "field2": "club2@gmail.com", "field3": "12"},
			{"field1": "Club 3", "field2": "club3@gmail.com", "field3": "3"},
			{"field1": "Club 4", "field2": "club4@gmail.com", "field3": "1"},
			{"field1": "Club 5", "field2": "club5@gmail.com", "field3": "16"},
			{"field1": "Club 6", "field2": "club6@gmail.com", "field3": "22"},
			{"field1": "Club 7", "field2": "club7@gmail.com", "field3": "3"}
		]
