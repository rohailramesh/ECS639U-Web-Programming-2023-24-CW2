<template>
  <form @submit.prevent="deleteClaim">
    <h2>Delete Demonstrator Claim</h2>
    <label for="claim_id">Enter Claim Form ID:</label>
    <input type="number" id="claim_id" v-model="claim_id" required />
    <button type="submit">Delete Claim</button>

    <div v-if="errorMessage">
      <p>{{ errorMessage }}</p>
    </div>
  </form>
</template>

<script>
export default {
  data() {
    return { claim_id: "", errorMessage: "" };
  },
  methods: {
    async deleteClaim() {
      this.errorMessage = ""; // Reset the error message
      if (!this.claim_id) {
        return;
      }

      // Send a DELETE request to your Django backend
      fetch(`http://localhost:8000/api/deleteClaim/${this.claim_id}`, {
        method: "DELETE",
      })
        .then((response) => {
          if (response.ok) {
            // Handle a successful deletion, e.g., show a success message
            console.log("Claim form deleted successfully");
            this.errorMessage = "Claim form deleted successfully";
          } else if (response.status === 404) {
            // Handle a 404 error, which indicates that the claim with the given ID was not found
            this.errorMessage =
              "Claim not found. Please enter a valid Claim ID.";
          } else {
            // Handle other error responses, e.g., show a general error message
            this.errorMessage = "Failed to delete claim form.";
          }
        })
        .catch((error) => {
          // Handle any errors, e.g., show an error message
          this.errorMessage = "An error occurred. Please try again.";
          console.error(error.message);
        });
    },
  },
};
</script>
