from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Simulates realistic user behavior

    @task(5)  # Highest priority (5x more likely)
    def load_homepage(self):
        self.client.get("/")

    @task(3)  # Higher weight (3x more likely to be tested)
    def load_training_list(self):
        self.client.get("/LawsRulesNIDCorrection.php")

    @task(2)  # Lower weight (2x)
    def load_fair_list(self):
        self.client.get("/ValidityNIDReRegistration.php")
