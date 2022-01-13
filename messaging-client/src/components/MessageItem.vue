<template>
  <div class="">
    <div
      v-bind:class="{ sent: message.sent, received: !message.sent }"
      class="message"
    >
      {{ message.text }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MessageItem',
  props: ['message'],
}
</script>

<style scoped>
.message {
  border-radius: 30px;
  padding: 15px;
  margin: 15px;
  max-width: 50%;
}

.sent {
  background: #0a7cff;
  color: #fff;
  float: right;
}

.received {
  background: #d0d0d0;
  color: #000;
}
</style>
