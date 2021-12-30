<template>
  <div class="container">
    <h2>Login and chat with your favorite people</h2>
    <div class="errors">
      <ul>
        <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
      </ul>
    </div>

    <form @submit.prevent="onSubmit" class="login-form">
      <input
        type="text"
        name="email-username"
        placeholder="Email or username"
        v-model="usernameOrEmail"
        required
      />

      <input
        type="password"
        placeholder="Password"
        v-model="password"
        required
      />
      <div class="btn-block">
        <button type="submit" class="btn">Login</button>
      </div>
    </form>

    <div>
      Dont have an account yet?
      <router-link to="/signup">Signup here</router-link>
    </div>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  name: 'Login',
  data() {
    return {
      usernameOrEmail: '',
      password: '',
      errors: [],
    }
  },
  methods: {
    async onSubmit() {
      if (this.usernameOrEmail === '' || this.password === '') {
        this.errors = ['All fields are required']
        return
      }
      try {
        const response = await axios.post('/auth/login', {
          usernameOrEmail: this.usernameOrEmail,
          password: this.password,
        })
        //TODO: Revisit this, use local storage for now
        localStorage.setItem('token', response.data.token)
        this.$router.push('/')
      } catch (error) {
        const errorData = error.response.data.errors
        if (errorData) {
          this.errors = errorData.map((error) => error.message)
        } else {
          this.errors = ['Oups, something went wwrong']
        }
      }
    },
  },
}
</script>

<style scope>
.errors {
  margin-top: 30px;
  color: #ff0000;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: 100vh;
}

.login-form {
  width: 300px;
  margin-top: 30px;
}

input {
  width: 100%;
  height: 40px;
  width: 100%;
  margin-bottom: 20px;
  border-radius: 4px;
  padding: 0 16px;
  font-size: 20px;
  border: 1px solid rgba(0, 0, 0, 0.2);
}

.btn-block {
  width: 100%;
  text-align: center;
  margin-bottom: 20px;
}
.btn {
  color: #fff;
  border-radius: 15px;
  background: #0a7cff;
  padding: 9.5px 20px;
  font-size: 15px;
  border: 0;
}
</style>
