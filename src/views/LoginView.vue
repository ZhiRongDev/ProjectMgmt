<template>
	<v-row class="d-flex justify-center">
		<v-col class="mt-5" cols="12" md="4">
			<h2 class="text-center">登入頁面</h2>
			<v-sheet rounded>
				<v-card class="px-6 py-8">
					<v-form v-model="form" @submit.prevent="onSubmit">
						<v-text-field v-model="User_Mail" :readonly="loading" :rules="[required]" class="mb-2" clearable
							label="Email"></v-text-field>

						<v-text-field v-model="User_Password" :readonly="loading" :rules="[required]" clearable
							label="Password" placeholder="Enter your password"></v-text-field>

						<br>
						<v-btn @click="signIn()" :disabled="!form" :loading="loading" block color="success" size="large" type="submit"
							variant="elevated">
							<strong>登入</strong>
						</v-btn>
						<br>
						<v-dialog v-model="dialog" persistent width="1024">
							<template v-slot:activator="{ props }">
								<v-btn block size="large" color="primary" v-bind="props">
									<strong>註冊</strong>
								</v-btn>
							</template>
							<v-card>
								<v-card-title>
									<span class="text-h5">User Profile</span>
								</v-card-title>
								<v-card-text>
									<v-container>
										<v-row>
											<v-col cols="12">
												<v-text-field v-model="cache.User_Name" label="Name*"
													hint="example of persistent helper text" persistent-hint
													required></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field v-model="cache.User_Mail" label="Email*" type="email"
													required></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field v-model="cache.User_Password" label="Password*"
													type="password" required></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field v-model="cache.User_Avatar" label="Avatar Url*"
													required></v-text-field>
											</v-col>
										</v-row>
									</v-container>
									<small>*indicates required field</small>
								</v-card-text>
								<v-card-actions>
									<v-spacer></v-spacer>
									<v-btn color="blue-darken-1" variant="text" @click="dialog = false; clearCache();">
										Close
									</v-btn>
									<v-btn color="blue-darken-1" variant="text" @click="signUp()">
										Save
									</v-btn>
								</v-card-actions>
							</v-card>
						</v-dialog>
					</v-form>
				</v-card>
			</v-sheet>
		</v-col>
	</v-row>

	<!-- 提示訊息 -->
	<v-snackbar v-model="snackbar" timeout="2000">
		{{ snackbar_msg }}
		<template v-slot:actions>
			<v-btn color="blue" variant="text" @click="snackbar = false">
				Close
			</v-btn>
		</template>
	</v-snackbar>
</template>

<style></style>

<script>
import axios from "axios";

export default {
	data: () => ({
		form: false,
		User_Mail: null,
		User_Password: null,
		loading: false,
		dialog: false,
		
		cache: {
			User_ID: "",
			User_Name: "",
			User_Mail: "",
			User_Avatar: "",
			User_Password: ""
		},

		snackbar_msg: "",
		snackbar: false,
	}),

	methods: {
		onSubmit() {
			if (!this.form) return
			this.loading = true
			setTimeout(() => (this.loading = false), 2000)
		},
		required(v) {
			return !!v || 'Field is required'
		},
		//
		clearCache() {
			let cache = {
				User_ID: "",
				User_Name: "",
				User_Mail: "",
				User_Avatar: "",
				User_Password: ""
			}
			this.cache = JSON.parse(JSON.stringify(cache)); // DeepCopy
		},

		signIn() {
			let self = this;
			let url = `${import.meta.env.VITE_FLASK_URL}/user/sign-in`;
			let data = {
				User_Mail: this.User_Mail,
				User_Password: this.User_Password,
			}
			axios.post(url, data)
				.then((res) => {
					console.log(res);
					let UserInfo = res.data.UserInfo;
					localStorage.setItem('UserInfo', JSON.stringify(UserInfo))
					this.$router.push({ path: '/home' })
				})
				.catch((err) => {
					// console.log(err);
					this.snackbar_msg = err.response.data;
					this.snackbar = true;
				})
		},

		signUp() {
			let self = this;
			let url = `${import.meta.env.VITE_FLASK_URL}/user/sign-up`;
			this.cache.User_ID = Date.now();
			let data = self.cache;

			axios.post(url, data)
				.then((res) => {
					// console.log(res);
					self.clearCache();
					this.snackbar_msg = err.response.data;
					this.dialog = false;
					this.snackbar = true;
				})
				.catch((err) => {
					this.snackbar_msg = err.response.data;
					this.snackbar = true;
				})
		}
	},
}
</script>