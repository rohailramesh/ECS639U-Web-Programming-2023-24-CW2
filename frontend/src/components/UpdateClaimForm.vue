<template>
  <div>
    <h2>Edit Claim Form</h2>
    <form @submit.prevent="fetchOldModuleName">
      <label for="claimId">Enter Claim ID to Update:</label>
      <input type="text" id="claim_id" v-model="claim_id" />
      <button type="submit">Find Claim Form</button>
    </form>

    <div v-if="errorMessage">
      <p>{{ errorMessage }}</p>
    </div>

    <div v-if="old_module_name">
      <label for="module_name">Old Module Name:</label>
      <p>{{ old_module_name }}</p>
      <form @submit.prevent="updateClaimForm">
        <label for="newModuleName">Enter New Module Name:</label>
        <input type="text" id="module_name" v-model="module_name" />
        <button type="submit">Update Claim Form</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      claim_id: "",
      module_name: "",
      old_module_name: "", // Store the old value
      errorMessage: "", // Store error message
    };
  },
  methods: {
    async fetchOldModuleName() {
      if (!this.claim_id) {
        this.errorMessage = ""; // Reset error message if claim_id is empty
        this.old_module_name = ""; // Reset old value if claim_id is empty
        return;
      }
      try {
        const response = await fetch(
          `http://localhost:8000/api/demonstrator_claim/${this.claim_id}`
        );
        if (response.ok) {
          const data = await response.json();
          this.old_module_name = data.module_name;
          this.errorMessage = ""; // Reset error message
        } else {
          // Handle error and show an error message
          this.errorMessage = "Claim not found. Please enter a valid Claim ID.";
          this.old_module_name = ""; // Reset old value
          console.error("Failed to fetch old module name");
        }
      } catch (error) {
        // Handle any other errors
        console.error(error);
        this.errorMessage = "An error occurred. Please try again.";
      }
    },
    async updateClaimForm() {
      if (!this.claim_id || !this.module_name) {
        return;
      }
      try {
        const response = await fetch(
          `http://localhost:8000/api/updateClaim/${this.claim_id}`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ module_name: this.module_name }),
          }
        );
        if (response.ok) {
          console.log("Claim form updated successfully");
        } else {
          console.error("Failed to update claim form");
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
