<template>
  <div>
    <h2>Get Demonstrator Claim</h2>
    <label for="claimId">Enter Claim ID:</label>
    <input type="text" id="claim_id" v-model="claimId" />
    <button @click="getClaimInfo">Get Claim Info</button>

    <div v-if="error">
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      claimId: "",
      error: "",
    };
  },
  methods: {
    async getClaimInfo() {
      this.error = ""; // Reset the error message

      try {
        const response = await fetch(
          `http://localhost:8000/api/demonstrator_claim/${this.claimId}`
        );
        if (response.ok) {
          const claimInfo = await response.json();
          this.$emit("claim-info", claimInfo); // Emit the claim info to the parent component
        } else if (response.status === 404) {
          this.error = "Claim not found. Please enter a valid Claim ID.";
        } else {
          this.error = "Failed to fetch claim information. Please try again.";
        }
      } catch (error) {
        this.error = "An error occurred. Please try again.";
      }
    },
  },
};
</script>
