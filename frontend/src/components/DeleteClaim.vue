<template>
  <form @submit.prevent="deleteClaim">
    <label for="claim_id">Enter Claim Form ID:</label>
    <input type="number" id="claim_id" v-model="claim_id" required />
    <button type="submit">Delete Claim</button>
  </form>
</template>

<script>
export default {
  data() {
    return { claim_id: "" };
  },
  methods: {
    async deleteClaim() {
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
          } else {
            // Handle an error response, e.g., show an error message
            console.error("Failed to delete claim form");
          }
        })
        .catch((error) => {
          // Handle any errors, e.g., show an error message
          console.error(error.message);
        });
    },
  },
};
</script>
