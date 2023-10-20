<template>
  <div class="container pt-3">
    <div class="h1 text-center border rounded bg-light p-2 mb-3">
      API Client
    </div>
    <div class="mb-3"><u>Response data</u>:</div>
    <div class="mb-3">
      <label for="claimId">Enter Claim ID:</label>
      <input type="text" id="claimId" v-model="claimId" />
      <button @click="getClaimInfo">Get Claim Info</button>
    </div>
    <p><strong>Module Name: </strong>{{ claim_info.module_name }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      response_data: "",
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
