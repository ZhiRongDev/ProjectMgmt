<template>
	<v-row class="d-flex justify-center">
		<v-col class="mt-5" cols="12" md="4">
			<h2 class="text-center">登入頁面</h2>
			<v-sheet rounded>
				<v-card class="px-6 py-8">
					<v-form v-model="form" @submit.prevent="onSubmit">
						<v-text-field v-model="email" :readonly="loading" :rules="[required]" class="mb-2" clearable
							label="Email"></v-text-field>

						<v-text-field v-model="password" :readonly="loading" :rules="[required]" clearable label="Password"
							placeholder="Enter your password"></v-text-field>

						<br>
						<v-btn :disabled="!form" :loading="loading" block color="success" size="large" type="submit"
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
												<v-text-field label="Name*" hint="example of persistent helper text"
													persistent-hint required></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field label="Email*" type="email" required></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field label="Password*" type="password" required></v-text-field>
											</v-col>
											<v-col cols="12">
												<v-text-field label="Avatar Url*" required></v-text-field>
											</v-col>
										</v-row>
									</v-container>
									<small>*indicates required field</small>
								</v-card-text>
								<v-card-actions>
									<v-spacer></v-spacer>
									<v-btn color="blue-darken-1" variant="text" @click="dialog = false">
										Close
									</v-btn>
									<v-btn color="blue-darken-1" variant="text" @click="dialog = false">
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

	<v-row justify="center">

	</v-row>
</template>

<style></style>

<script>
export default {
	data: () => ({
		form: false,
		email: null,
		password: null,
		loading: false,
		dialog: false,
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
	},
}
</script>