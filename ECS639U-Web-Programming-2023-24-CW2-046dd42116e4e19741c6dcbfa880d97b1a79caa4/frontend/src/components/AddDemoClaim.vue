<template>
  <div class="container">
    <form @submit.prevent="addClaim">
      <div class="mb-3">
        <label for="module_name" class="form-label">Module Name:</label>
        <input
          type="text"
          id="module_name"
          v-model="module_name"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3">
        <label for="hours_worked" class="form-label">Hours Worked:</label>
        <input
          type="number"
          id="hours_worked"
          v-model="hours_worked"
          class="form-control"
          required
        />
      </div>

      <div class="mb-3 form-check">
        <input
          type="checkbox"
          id="claim_form_submitted"
          v-model="claim_form_submitted"
          class="form-check-input"
        />
        <label for="claim_form_submitted" class="form-check-label"
          >QM Claim Form Submitted</label
        >
      </div>

      <div class="mb-3">
        <label for="demonstrated_date" class="form-label"
          >Demonstrated Date:</label
        >
        <input
          type="date"
          id="demonstrated_date"
          v-model="demonstrated_date"
          class="form-control"
          required
        />
      </div>

      <button type="submit" class="button">Add Claim</button>
    </form>

    <div v-if="successMessage" class="alert alert-success mt-3">
      <p>{{ successMessage }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      module_name: "",
      hours_worked: null,
      claim_form_submitted: false,
      demonstrated_date: "",
      successMessage: "",
    };
  },
  methods: {
    addClaim() {
      const claimData = {
        module_name: this.module_name,
        hours_worked: this.hours_worked,
        claim_form_submitted: this.claim_form_submitted,
        demonstrated_date: this.demonstrated_date,
      };

      // Make a POST request to your Django backend API
      fetch("http://localhost:8000/api/addDemoClaim", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(claimData),
      })
        .then((response) => {
          if (response.ok) {
            // Handle a successful response
            this.successMessage = "Claim Form added successfully!";
            setTimeout(() => {
              this.successMessage = ""; // Clear success message after 5 seconds
            }, 2000);
            return response.json();
          } else {
            // Handle an error response
            throw new Error("Failed to add claim");
          }
        })
        .then((data) => {
          // Handle the response data, e.g., show a success message
          console.log(data.message);
        })
        .catch((error) => {
          // Handle any errors, e.g., show an error message
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
