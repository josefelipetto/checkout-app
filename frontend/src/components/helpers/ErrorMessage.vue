<template>
  <div id="api-error">
    <div class="py-5 bg-light">
      <div class="container">
        <div class="px-4 py-5 my-5 text-center">
          <img class="d-block mx-auto mb-4" src="@/assets/error-icon.png" alt="" width="100" height="100">
          <h1 class="display-5 fw-bold">{{ title }}</h1>
          <div class="col-lg-6 mx-auto">
            <p class="lead mb-4">{{ text }}</p>
            <div class="d-grid gap-2 d-sm-flex justify-content-sm-center" v-if="reloadButton">
              <button type="button" class="btn btn-primary btn-lg px-4 gap-3" @click="reload">Reload the page</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/**
 * Error message component, used when there is some error
 * @displayName Error message
 */
export default {
  name: 'ErrorMessage',
  props: {
    /**
     * Title property
     */
    title: String,
    /**
     * Text property
     */
    text: String,
    /**
     * Determine if a reload page button should be displayed
     */
    reloadButton: Boolean
  },
  methods: {
    /**
     * Reload the page
     */
    reload () {
      this.$router.go(0)
    }
  }
}
</script>
