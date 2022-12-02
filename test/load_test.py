from locust import HttpUser, task, constant

class reportService(HttpUser):

  wait_time = constant(2)

  @task
  def generate_report(self):
    resp = self.client.post("/report")
    if resp.status_code != 200:
      print("Error generating report")