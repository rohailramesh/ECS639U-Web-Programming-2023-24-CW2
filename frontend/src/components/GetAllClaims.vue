<template>
  <div>
    <h2>Get All Claims</h2>
    <div v-if="claims.length > 0">
      <ul>
        <li v-for="claim in claims" :key="claim.id">
          <p><strong>Claim ID:</strong> {{ claim.id }}</p>
          <p><strong>Module Name:</strong> {{ claim.module_name }}</p>
          <p><strong>Hours Worked:</strong> {{ claim.hours_worked }}</p>
          <p>
            <strong>Claim Form Submitted:</strong>
            {{ claim.claim_form_submitted }}
          </p>
          <p>
            <strong>Demonstrated Date:</strong> {{ claim.demonstrated_date }}
          </p>
          <hr />
        </li>
      </ul>
    </div>
    <div v-else>
      <p>No claims found.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      claims: [], // To store the list of claims
    };
  },
  mounted() {
    // Fetch all claims from your API endpoint when the component is mounted
    this.fetchAllClaims();
  },
  methods: {
    async fetchAllClaims() {
      try {
        const response = await fetch(`http://localhost:8000/api/allClaims`);
        if (response.ok) {
          const data = await response.json();
          this.claims = data;
        } else {
          // Handle error, e.g., show an error message
          console.error("Failed to fetch claims");
        }
      } catch (error) {
        // Handle any other errors, e.g., network issues
        console.error(error);
      }
    },
  },
};
</script>
