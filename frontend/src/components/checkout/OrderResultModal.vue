<template>
  <div class="modal fade" id="success-modal" tabindex="-1" aria-labelledby="successModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-confirm" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <div class="icon-box" :style="`--backgroundColor: ${computedBackgroundColor}`">
            <i class="material-icons">
              <BIconCheckLg />
            </i>
          </div>
          <h4 class="modal-title w-100">{{ computedTitle }}</h4>
        </div>
        <div class="modal-body">
          <p class="text-center">{{ computedText }}</p>
        </div>
        <div class="modal-footer">
          <button
            class="btn btn-success btn-block"
            data-dismiss="modal"
            @click="hide"
            :style="`--backgroundColor: ${computedBackgroundColor}; --backgroundFocusColor: ${computedBackgroundFocusColor}`"
          >
            OK
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Modal } from 'bootstrap'
import { BIconCheckLg } from 'bootstrap-icons-vue'

/**
 * Modal responsible for comunicate order success or fail message
 * @displayName Order Confirmed Modal
*/
export default {
  name: 'OrderConfirmedModal',
  props: {
    /**
     * The url that should redirects in case of success after the `Ok` button is pressed
     */
    onSuccessRedirectTo: String
  },
  data: () => ({
    modal: null,
    type: '',
    title: '',
    text: ''
  }),
  methods: {
    /**
     * Shows the modal on the screen
     */
    show () {
      this.modal.show()
    },
    /**
     * Hides the modal on the screen
     */
    hide () {
      this.modal.hide()
      if (this.type === 'S') {
        this.$router.push(this.onSuccessRedirectTo)
      }
    },
    /**
     * Set current type, whether is Success 'S' or Fail 'F'
     * @param type
     */
    setType (type) {
      this.type = type
    }
  },
  mounted () {
    this.modal = new Modal(document.getElementById('success-modal'))
  },
  computed: {
    /**
     * Return the modal items background color based on type.
     */
    computedBackgroundColor () {
      return this.type === 'S' ? '#82ce34' : '#ce4234'
    },
    /**
     * Returns the background of the confirm button when focused based on type.
     */
    computedBackgroundFocusColor () {
      return this.type === 'S' ? '#6fb32b' : '#b32b2b'
    },
    /**
     * Returns the title of the modal based on type
     */
    computedTitle () {
      return this.type === 'S' ? 'Awesome!' : 'Whoops :('
    },
    /**
     * Returns the text of the modal based on type
     */
    computedText () {
      return this.type === 'S'
        ? 'Your order has been confirmed and we already started to make your meal.'
        : 'Something did not go well. Try again in a few moments. We apologize for the inconvenience.'
    }
  },
  components: {
    BIconCheckLg
  }
}
</script>

<style scoped>
.modal-confirm {
  color: #636363;
  width: 325px;
  font-size: 14px;
}
.modal-confirm .modal-content {
  padding: 20px;
  border-radius: 5px;
  border: none;
}
.modal-confirm .modal-header {
  border-bottom: none;
  position: relative;
}
.modal-confirm h4 {
  text-align: center;
  font-size: 26px;
  margin: 30px 0 -15px;
}
.modal-confirm .form-control, .modal-confirm .btn {
  min-height: 40px;
  border-radius: 3px;
}
.modal-confirm .close {
  position: absolute;
  top: -5px;
  right: -5px;
}
.modal-confirm .modal-footer {
  border: none;
  text-align: center;
  border-radius: 5px;
  font-size: 13px;
}
.modal-confirm .icon-box {
  --backgroundColor: #82ce34;
  color: #fff;
  position: absolute;
  margin: 0 auto;
  left: 0;
  right: 0;
  top: -70px;
  width: 95px;
  height: 95px;
  border-radius: 50%;
  z-index: 9;
  background: var(--backgroundColor);
  padding: 15px;
  text-align: center;
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.1);
}
.modal-confirm .icon-box i {
  font-size: 58px;
  position: relative;
  top: -12px;
}
.modal-confirm.modal-dialog {
  margin-top: 80px;
}
.modal-confirm .btn {
  --backgroundColor: #82ce34;
  color: #fff;
  border-radius: 4px;
  background: var(--backgroundColor);
  text-decoration: none;
  transition: all 0.4s;
  line-height: normal;
  border: none;
}
.modal-confirm .btn:hover, .modal-confirm .btn:focus {
  --backgroundFocusColor: #6fb32b;
  background: var(--backgroundFocusColor);
  outline: none;
}
.trigger-btn {
  display: inline-block;
  margin: 100px auto;
}
</style>
