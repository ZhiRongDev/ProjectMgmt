<template>
	<main>
		<AppWrapper>
			<v-container>
				<v-row>
					<v-col class="mt-2" cols="12">
						<h2>你的專案</h2>
					</v-col>
					<v-col v-for="(item, j) in Project" :key="item.Project_ID" cols="12" sm="6" md="4">
						<div>
							<v-hover v-slot="{ isHovering, props }">
								<v-card class="mx-auto" height="200" v-bind="props" :color="item.Project_Color">
									<!-- <v-img src="https://cdn.vuetifyjs.com/images/cards/forest-art.jpg"></v-img> -->

									<v-card-text class="d-flex justify-center align-center h-100">
										<div>
											<v-chip size="x-large" variant="elevated">
												{{ item.Project_Name }}
											</v-chip>
										</div>
									</v-card-text>

									<v-overlay :model-value="isHovering" contained scrim="#036358"
										class="align-center justify-center">
										<v-row>
											<v-col>
												<v-btn variant="flat" color="secondary"
													@click="open_dialog_setting(type='update', target = item)">更改</v-btn>
											</v-col>
											<v-col>
												<v-btn variant="flat" color="primary" @click="goToProject(item)">進入</v-btn>
											</v-col>
											<v-col>
												<v-btn variant="flat" color="red"
													@click="cache.Project_ID = item.Project_ID; dialog_delete = true;">刪除</v-btn>
											</v-col>
										</v-row>
									</v-overlay>
								</v-card>
							</v-hover>
						</div>
					</v-col>

					<!-- 新增專案 -->
					<v-col cols="12" sm="6" md="4">
						<v-btn block class="mx-auto" height="200" @click="open_dialog_setting()">
							<v-icon size="x-large" style="font-size: 40px;">mdi-plus</v-icon>
							<v-tooltip activator="parent" location="top"> 新增專案 </v-tooltip>
						</v-btn>
					</v-col>
				</v-row>
			</v-container>
		</AppWrapper>

		<!-- 新增、更新專案 -->
		<v-dialog v-model="dialog_setting" class="dialog_sizing" persistent>
			<v-card>
				<v-card-text>
					<v-container>
						<h3 class="mb-3">
							專案設定
						</h3>
						<v-row>
							<v-col cols="12">
								<v-text-field v-model="cache.Project_Name" label="專案名稱*" type="text" required></v-text-field>
							</v-col>
							<v-col cols="12">
								<p class="mb-1"><strong>專案顏色</strong></p>
								<v-color-picker v-model="cache.Project_Color" elevation="0"></v-color-picker>
								{{ cache.Project_Color }}
							</v-col>
						</v-row>
					</v-container>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn color="red" variant="text" @click="clearCache(); dialog_setting = false">
						Disagree
					</v-btn>
					<v-btn color="green-darken-1" variant="text" @click="set_Project()">
						Agree
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>

		<!-- 刪除專案 -->
		<v-dialog v-model="dialog_delete" width="auto" persistent>
			<v-card>
				<v-card-text>
					你確定要刪除專案 ?
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn color="red" variant="text" @click="clearCache(); dialog_delete = false">
						Disagree
					</v-btn>
					<v-btn color="green-darken-1" variant="text" @click="delete_Project()">
						Agree
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>

		<!-- 提示訊息 -->
		<v-snackbar v-model="snackbar" timeout="2000">
			{{ snackbar_msg }}
			<template v-slot:actions>
				<v-btn color="blue" variant="text" @click="snackbar = false">
					Close
				</v-btn>
			</template>
		</v-snackbar>
	</main>
</template>

<script>
import axios from 'axios';
import { mapState, mapActions } from 'pinia'
import UserStatus from '@/stores/UserStatus'
import AppWrapper from '../components/AppWrapper.vue';
import { ThirdPartyDraggable } from '@fullcalendar/interaction';

export default {
	data: () => ({
		dialog_setting: false,
		dialog_delete: false,
		dialog_setting_type: "",
		
		snackbar_msg: "",
		snackbar: false,
		
		Project: [],
		
		cache: {
			Project_ID: "",
			Project_Name: "",
			Project_Color: "",
		}
	}),
	components: {
		AppWrapper
	},
	computed: {
		...mapState(UserStatus, ['User'])
	},
	methods: {
		...mapActions(UserStatus, ['checkAuth']),
		getProject_List() {
			let self = this;
			let url = `${import.meta.env.VITE_FLASK_URL}/Project?User_ID=${this.User.User_ID}`;
			axios.get(url)
				.then(function (res) {
					console.log(res);
					self.Project = res.data.return_data;
				})
				.catch(function (err) {
					console.log(err);
				})
		},

		goToProject(target) {
			this.$router.push({ path: '/project', query: { User_ID: this.User.User_ID, Project_ID: target.Project_ID } })
		},

		clearCache() {
			let cache = {
				Project_ID: "",
				Project_Name: "",
				Project_Color: "",
			}
			this.cache = JSON.parse(JSON.stringify(cache)); // DeepCopy
		},

		open_dialog_setting(type="new", target = {}) {
			this.dialog_setting_type = type;
			this.cache.Project_ID = target.Project_ID;
			this.cache.Project_Name = target.Project_Name;
			this.cache.Project_Color = target.Project_Color;
			this.dialog_setting = true;
		},

		new_Project() {
			let self = this;
			let url = `${import.meta.env.VITE_FLASK_URL}/Project?User_ID=${this.User.User_ID}`;
			self.cache.Project_ID = Date.now();
			let data = self.cache;

			axios.post(url, data)
				.then(function (res) {
					console.log(res);
					self.snackbar_msg = res.data.response;
					self.snackbar = true;
					self.getProject_List();
				})
				.catch(function (err) {
					self.snackbar_msg = err.response.data;
					self.snackbar = true;
				})
			
			this.dialog_setting = false
		},

		update_Project() {
			let self = this;
			let url = `${import.meta.env.VITE_FLASK_URL}/Project?User_ID=${this.User.User_ID}`;
			let data = self.cache;
			axios.put(url, data)
				.then(function (res) {
					console.log(res);
					self.snackbar_msg = res.data.response;
					self.snackbar = true;
					self.getProject_List();
				})
				.catch(function (err) {
					console.log(err);
					self.snackbar_msg = err.response.data;
					self.snackbar = true;
					console.log(err);
				})
			
			this.dialog_setting = false
		},

		set_Project() {
			if(this.dialog_setting_type == "new") {
				this.new_Project();
			} else if (this.dialog_setting_type == "update") {
				this.update_Project();
			}
		},

		delete_Project() {
			// console.log(this.cache.Project_ID);
			let self = this;
			let url = `${import.meta.env.VITE_FLASK_URL}/Project?User_ID=${this.User.User_ID}&Project_ID=${this.cache.Project_ID}`;
			axios.delete(url)
				.then(function (res) {
					console.log(res);
					self.snackbar_msg = res.data.response;
					self.snackbar = true;
					self.getProject_List();
				})
				.catch(function (err) {
					console.log(err);
					self.snackbar_msg = err.response.data;
					self.snackbar = true;
				})

			this.clearCache();
			this.dialog_delete = false;
		}

	},
	mounted() {
		(async () => {
			await this.checkAuth();
			await this.getProject_List();
		})();
	}
}
</script>

<style>
/* Small devices */
@media (min-width: 576px) {}

/* Medium devices */
@media (min-width: 768px) {
	.dialog_sizing {
		width: 80%;
	}
}

/* Large devices */
@media (min-width: 992px) {
	.dialog_sizing {
		width: 50%;
	}
}
</style>