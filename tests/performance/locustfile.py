from locust import HttpUser, task


class PerfTest(HttpUser):
	"""
	Performance tests on main urls
	"""

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
		self.client.post("/show_summary", data={"email": "locust@gmail.com"})

	@task
	def perf_book(self):
		self.client.get("/book/Competition Locust/Club Locust")

	@task
	def perf_purchase(self):
		self.client.post("/purchase_places", data={"competition": "Competition Locust", "club": "Club Locust", "places": 0})
