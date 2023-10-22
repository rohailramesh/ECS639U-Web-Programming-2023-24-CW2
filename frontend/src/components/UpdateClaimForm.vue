<template>
  <div>
    <h2>Update Demonstrator Claim</h2>
    <form @submit.prevent="fetchOldClaimInfo">
      <label for="claimId">Enter Claim ID to Update:</label>
      <input type="text" id="claim_id" v-model="claim_id" />
      <button type="submit">Find Claim Form</button>
    </form>

    <div v-if="errorMessage">
      <p>{{ errorMessage }}</p>
    </div>

    <div v-if="old_claim_info">
      <h3>Old Claim Information:</h3>
      <form @submit.prevent="updateClaimForm">
        <label for="module_name">Module Name:</label>
        <input
          type="text"
          id="module_name"
          v-model="old_claim_info.module_name"
        />
        <label for="hours_worked">Hours Worked:</label>
        <input
          type="number"
          id="hours_worked"
          v-model="old_claim_info.hours_worked"
        />
        <label for="claim_form_submitted">Claim Form Submitted:</label>
        <input
          type="checkbox"
          id="claim_form_submitted"
          v-model="old_claim_info.claim_form_submitted"
        />
        <label for="demonstrated_date">Demonstrated Date:</label>
        <input
          type="date"
          id="demonstrated_date"
          v-model="old_claim_info.demonstrated_date"
        />

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
      old_claim_info: null,
      errorMessage: "",
    };
  },
  methods: {
    async fetchOldClaimInfo() {
      if (!this.claim_id) {
        this.errorMessage = "";
        this.old_claim_info = null;
        return;
      }
      try {
        const response = await fetch(
          `http://localhost:8000/api/demonstrator_claim/${this.claim_id}`
        );
        if (response.ok) {
          const data = await response.json();
          this.old_claim_info = data;
          this.errorMessage = "";
        } else {
          this.errorMessage = "Claim not found. Please enter a valid Claim ID.";
          this.old_claim_info = null;
          console.error("Failed to fetch old claim information");
        }
      } catch (error) {
        console.error(error);
        this.errorMessage = "An error occurred. Please try again.";
      }
    },
    async updateClaimForm() {
      if (!this.claim_id) {
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
            body: JSON.stringify(this.old_claim_info),
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
