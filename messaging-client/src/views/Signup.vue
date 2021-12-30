<template>
  <div class="container">
    <h2>Signup and chat with your favorite people</h2>
    <div class="errors">
      <ul>
        <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
      </ul>
    </div>
    <form @submit.prevent="onSubmit" class="login-form">
      <input
        type="text"
        name="username"
        placeholder="Enter username"
        v-model="username"
        required
      />

      <input
        type="email"
        name="email"
        placeholder="Enter email address"
        v-model="email"
        required
      />

      <input
        type="password"
        placeholder="Enter password"
        v-model="password"
        required
      />

      <input
        type="password"
        placeholder="Confirm password"
        v-model="passwordConfirmation"
        required
      />
      <div class="btn-block">
        <button type="submit" class="btn">Signup</button>
      </div>
    </form>

    <div>
      Already have an account? <router-link to="/login">Login here</router-link>
    </div>
  </div>
</template>

<script>
import axios from '../axios'

export default {
  name: 'Signup',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      passwordConfirmation: '',
      errors: [],
    }
  },
  methods: {
    async onSubmit() {
      if (
        this.username === '' ||
        this.email === '' ||
        this.password === '' ||
        this.passwordConfirmation === ''
      ) {
        this.errors = ['A field cannot be empty']
        return
      }

      if (this.password.length < 8) {
        this.errors = ['Password must have at least 8 characters']
        return
      }

      if (this.password !== this.passwordConfirmation) {
        this.errors = ['Passwords do not match']
        return
      }

      //TODO: save user information after i implement login on backend
      try {
        const response = await axios.post('/auth/signup', {
          username: this.username,
          email: this.email,
          password: this.password,
        })
        //TODO: Revisit this, use local storage for now
        localStorage.setItem('token', response.data.token)
        this.$router.push('/')
      } catch (error) {
        const errorData = error.response.data.errors
        console.log(error.response.data)
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
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  min-height: 100vh;
}

.errors {
  margin-top: 30px;
  color: #ff0000;
}

.login-form {
  width: 300px;
  margin-top: 30px;
}
input {
  width: 100%;
  height: 40px;
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
