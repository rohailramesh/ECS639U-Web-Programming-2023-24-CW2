<template>
  <form @submit.prevent="deleteClaim">
    <div class="mb-3">
      <label for="claim_id" class="form-label">Enter Claim Form ID:</label>
      <input
        type="number"
        id="claim_id"
        v-model="claim_id"
        class="form-control"
        required
      />
    </div>

    <button type="submit" class="button">Delete Claim</button>

    <div class="mt-3" v-if="errorMessage">
      <div class="alert alert-danger">{{ errorMessage }}</div>
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

<style>
.button {
  background-color: #a79d88;
  border-radius: 10px;
  border-width: 0;
  display: inline-block;
  font-weight: 400;
  text-align: center;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  color: #fff;
  margin-right: 10px;
}
</style>
