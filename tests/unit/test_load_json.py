from ... import server


class TestLoadClass:

	load_dataset = [
		{"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"},
		{"name": "Iron Temple", "email": "admin@irontemple.com", "points": "4"},
		{"name": "She Lifts", "email": "kate@shelifts.co.uk", "points": "12"}
	]

	def test_load_json(self):
		assert server.load_json("tests/unit/load_dataset") == self.load_dataset
