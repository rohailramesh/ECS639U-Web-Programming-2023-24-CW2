<template>
  <div class="card mb-4">
    <div class="card-body">
      <h5 class="card-title">Claim ID: {{ claim.id }}</h5>
      <p class="card-text">
        <strong>Module Name:</strong> {{ claim.module_name }}
      </p>
      <p class="card-text">
        <strong>Hours Worked:</strong> {{ claim.hours_worked }}
      </p>
      <p class="card-text">
        <strong>Claim Form Submitted:</strong>
        <span v-if="claim.claim_form_submitted">Yes</span>
        <span v-else>No</span>
      </p>
      <p class="card-text">
        <strong>Demonstrated Date:</strong> {{ claim.demonstrated_date }}
      </p>
      <button @click="deleteClaim" class="button">Delete Claim</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    claim: Object, // Claim data passed as a prop
  },
  methods: {
    deleteClaim() {
      // Trigger the deletion of the corresponding claim by emitting an event
      this.$emit("delete-claim", this.claim.id);
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
}
</style>
