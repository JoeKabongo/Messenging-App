<template>
  <section>
    <!-- <div> -->
    <div class="messages">
      <div v-for="message in messages" :key="message.text">
        <MessageItem :message="message" />
        <!-- {{ message.text }} -->
      </div>
    </div>
    <div id="new-message-div">
      <textarea v-model="newMessage"></textarea>
      <button @click="onNewMessage">Send</button>
    </div>
    <!-- </div> -->
  </section>
</template>

<script>
import MessageItem from './MessageItem.vue'
export default {
  components: { MessageItem },
  name: 'Messages',
  methods: {
    onNewMessage() {
      if (!this.newMessage) {
        return
      }
      // Send new message here
      this.messages.push({
        text: this.newMessage,
        sent: true,
      })
      this.newMessage = ''
    },
  },
  data() {
    return {
      newMessage: '',
      messages: [
        {
          text: 'Hey, whats up',
          sent: true,
        },
        {
          text: 'Me mememe',
          sent: false,
        },

        {
          text: 'Me mememe',
          sent: true,
        },

        {
          text: 'Me mememe',
          sent: false,
        },

        {
          text: 'I saw him today, it was hilarioous',
          sent: false,
        },

        {
          text: 'Me mememe',
          sent: true,
        },
        {
          text: 'Hey, whats up',
          sent: true,
        },
        {
          text: 'Me mememe',
          sent: false,
        },

        {
          text: 'Me mememe',
          sent: true,
        },

        {
          text: 'Me mememe',
          sent: false,
        },

        {
          text: 'I saw him today, it was hilarioous',
          sent: false,
        },

        {
          text: 'Me mememe',
          sent: true,
        },
        {
          text: 'Hey, whats up',
          sent: true,
        },
        {
          text: 'Me mememe',
          sent: false,
        },

        {
          text: 'Me mememe',
          sent: true,
        },

        {
          text: 'Me mememe',
          sent: false,
        },

        {
          text: 'I saw him today, it was hilarioous',
          sent: false,
        },

        {
          text: 'Me mememe',
          sent: true,
        },
      ],
    }
  },
}
</script>

<style scoped>
section {
  height: 100vh;
  margin-left: 300px;
  position: relative;
}

.messages {
  display: flex;
  flex-direction: column;
  margin-top: 100px;
}

#new-message-div {
  position: fixed;
  bottom: 0;
  width: 800px;
  padding: 10px;
}

textarea {
  width: 100%;
  min-height: 70;
  max-height: 100px;
  border-radius: 20px;
  background: #ebebeb;
  padding: 10px;
}

button {
  color: #fff;
  border-radius: 15px;
  background: #0a7cff;
  padding: 9.5px 20px;
  font-size: 15px;
  border: 0;
  cursor: pointer;
}
</style>
