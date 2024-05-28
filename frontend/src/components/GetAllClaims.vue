<template>
  <div class="allClaims">
    <h2>Rohail's Claims</h2>
    <div v-if="claims.length > 0">
      <div class="row">
        <div class="col-md-4" v-for="claim in claims" :key="claim.id">
          <!-- Use the ClaimCard component to display each claim -->
          <claim-card-vue
            :claim="claim"
            @delete-claim="deleteClaim(claim.id)"
          />
        </div>
      </div>
    </div>
    <div v-else>
      <p>No claims found.</p>
    </div>
  </div>
</template>

<script>
import ClaimCardVue from "./ClaimCard.vue";
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
  components: {
    ClaimCardVue, // Register the new component
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
    async deleteClaim(claimId) {
      try {
        // Make a DELETE request to delete the claim
        const response = await fetch(
          `http://localhost:8000/api/deleteClaim/${claimId}`,
          {
            method: "DELETE",
          }
        );

        if (response.ok) {
          // Remove the deleted claim from the list
          this.claims = this.claims.filter((claim) => claim.id !== claimId);
          console.log("Claim deleted successfully");
        } else if (response.status === 404) {
          console.error("Claim not found. Please enter a valid Claim ID.");
        } else {
          console.error("Failed to delete claim form.");
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>
<style>
.allClaims {
  margin-bottom: 300px;
}
</style>
