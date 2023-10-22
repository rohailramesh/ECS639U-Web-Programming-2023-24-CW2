<template>
  <div>
    <h2>Add Demonstrator Claim</h2>
    <form @submit.prevent="addClaim">
      <label for="module_name">Module Name:</label>
      <input type="text" id="module_name" v-model="module_name" required />

      <label for="hours_worked">Hours Worked:</label>
      <input type="number" id="hours_worked" v-model="hours_worked" required />

      <label for="claim_form_submitted">QM Claim Form Submitted:</label>
      <input
        type="checkbox"
        id="claim_form_submitted"
        v-model="claim_form_submitted"
      />

      <label for="demonstrated_date">Demonstrated Date:</label>
      <input
        type="date"
        id="demonstrated_date"
        v-model="demonstrated_date"
        required
      />

      <button type="submit">Add Claim</button>
    </form>
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
