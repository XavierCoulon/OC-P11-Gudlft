from locust import HttpUser, task
#from ... import server


class PerfTest(HttpUser):
	@task
	def perf_index(self):
		self.client.get("/")

	@task
	def perf_logout(self):
		self.client.get("/logout")

	@task
	def perf_points(self):
		self.client.get("/points")

	@task
	def perf_login(self):
		self.client.post("/show_summary", data={"email": "john@simplylift.co"})

	@task
	def perf_book(self):
		self.client.get("/book/Spring Festival/Simply Lift")

	@task
	def perf_purchase(self):
		self.client.post("/purchase_places", data={"competition": "Spring Festival", "club": "Simply Lift", "places": 0})
