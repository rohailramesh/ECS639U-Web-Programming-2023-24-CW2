<template>
  <div class="container">
    <div class="mb-3">
      <label for="claimId" class="form-label">Enter Claim ID:</label>
      <input type="text" id="claim_id" v-model="claimId" class="form-control" />
    </div>
    <br />
    <button @click="getClaimInfo" class="button">Get Claim Info</button>

    <div class="mt-3" v-if="error">
      <div class="alert alert-danger">{{ error }}</div>
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
          // console.log(claimInfo);
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
