<template>
  <div>
    <label for="claimId">Enter Claim ID:</label>
    <input type="text" id="claimId" v-model="claimId" />
    <button @click="getClaimInfo">Get Claim Info</button>
    <p><strong>Module Name: </strong>{{ claim_info.module_name }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      claim_info: {},
      claimId: "",
    };
  },
  methods: {
    async getClaimInfo() {
      if (!this.claimId) {
        return;
      }
      const response = await fetch(
        `http://localhost:8000/api/demonstrator_claim/${this.claimId}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      this.claim_info = await response.json();
    },
  },
};
</script>
