from locust import HttpUser, task


class reportService(HttpUser):
    
    def generate_report(self):
        resp = self.client.post("report")
        if resp.status_code != 200:
            print("Error generating report")
        return resp
    
    @task
    def generate_flow(self):
        self.generate_report()

    
