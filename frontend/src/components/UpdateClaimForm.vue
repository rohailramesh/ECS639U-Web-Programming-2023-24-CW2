<template>
  <div class="container">
    <form @submit.prevent="fetchOldClaimInfo" class="mb-3">
      <label for="claimId" class="form-label">Enter Claim ID to Update:</label>
      <input
        type="text"
        id="claim_id"
        v-model="claim_id"
        class="form-control"
      />
      <br />
      <button type="submit" class="button">Find Claim Form</button>
    </form>

    <div v-if="errorMessage" class="alert alert-danger mt-3">
      <p>{{ errorMessage }}</p>
    </div>

    <div v-if="old_claim_info">
      <h3>Old Claim Information:</h3>

      <form @submit.prevent="updateClaimForm" class="mt-3">
        <div class="mb-3">
          <label for="module_name" class="form-label">Module Name:</label>
          <input
            type="text"
            id="module_name"
            v-model="old_claim_info.module_name"
            class="form-control"
          />
        </div>

        <div class="mb-3">
          <label for="hours_worked" class="form-label">Hours Worked:</label>
          <input
            type="number"
            id="hours_worked"
            v-model="old_claim_info.hours_worked"
            class="form-control"
          />
        </div>

        <div class="mb-3 form-check">
          <input
            type="checkbox"
            id="claim_form_submitted"
            v-model="old_claim_info.claim_form_submitted"
            class="form-check-input"
          />
          <label for="claim_form_submitted" class="form-check-label"
            >Claim Form Submitted</label
          >
        </div>

        <div class="mb-3">
          <label for="demonstrated_date" class="form-label"
            >Demonstrated Date:</label
          >
          <input
            type="date"
            id="demonstrated_date"
            v-model="old_claim_info.demonstrated_date"
            class="form-control"
          />
        </div>
        <br />
        <button type="submit" class="button">Update Claim Form</button>
      </form>
      <div v-if="successMessage" class="alert alert-success mt-3">
        <p>{{ successMessage }}</p>
      </div>
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
      successMessage: "",
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
          this.successMessage = "Claim Form updated successfully!";
          setTimeout(() => {
            this.successMessage = ""; // Clear success message after 5 seconds
          }, 2000);
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
