<template>
  <section class="py-2 text-center container">
      <div class="row py-lg-5">
        <div class="col-lg-6 col-md-8 mx-auto">
          <h1 class="fw-normal">{{ title }}</h1>
          <p class="lead text-muted">{{ text }}</p>
        </div>
      </div>
    </section>
</template>

<script>
/**
 * Marketing Call component
 * @displayName Marketing Call
 */
export default {
  name: 'MarketingCall',
  props: {
    /**
     * Title property
     */
    title: String,
    /**
     * Text property
     */
    text: String
  }
}
</script>

<style scoped>

</style>
