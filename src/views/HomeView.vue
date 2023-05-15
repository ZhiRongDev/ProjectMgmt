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
													@click="dialog_update = true">更改</v-btn>
											</v-col>
											<v-col>
												<v-btn variant="flat" color="primary">進入</v-btn>
											</v-col>
											<v-col>
												<v-btn variant="flat" color="red" @click="dialog_delete = true">刪除</v-btn>
											</v-col>
										</v-row>
									</v-overlay>
								</v-card>
							</v-hover>
						</div>
					</v-col>

					<!-- 新增專案 -->
					<v-col cols="12" sm="6" md="4">
						<v-btn block class="mx-auto" height="200" @click="dialog_create = true">
							<v-icon size="x-large" style="font-size: 40px;">mdi-plus</v-icon>
							<v-tooltip activator="parent" location="top"> 新增專案 </v-tooltip>
						</v-btn>
					</v-col>
				</v-row>
			</v-container>
		</AppWrapper>

		<!-- 新增專案 -->
		<v-dialog v-model="dialog_create" class="dialog_sizing" persistent>
			<v-card>
				<v-card-text>
					<v-container>
						<h3 class="mb-3">
							新增專案
						</h3>
						<v-row>
							<v-col cols="12">
								<v-text-field label="專案名稱*" type="password" required></v-text-field>
							</v-col>
							<v-col cols="12">
								<p class="mb-1"><strong>專案顏色</strong></p>
								<v-color-picker v-model="color_picker" elevation="0"></v-color-picker>
								{{ color_picker }}
							</v-col>
						</v-row>
					</v-container>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn color="red" variant="text" @click="dialog_create = false">
						Disagree
					</v-btn>
					<v-btn color="green-darken-1" variant="text" @click="dialog_create = false">
						Agree
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>

		<!-- 更新專案 -->
		<v-dialog v-model="dialog_update" class="dialog_sizing" persistent>
			<v-card>
				<v-card-text>
					<v-container>
						<h3 class="mb-3">
							更新專案
						</h3>
						<v-row>
							<v-col cols="12" sm="6" md="4">
								<v-text-field label="Legal first name*" required></v-text-field>
							</v-col>
							<v-col cols="12" sm="6" md="4">
								<v-text-field label="Legal middle name"
									hint="example of helper text only on focus"></v-text-field>
							</v-col>
							<v-col cols="12" sm="6" md="4">
								<v-text-field label="Legal last name*" hint="example of persistent helper text"
									persistent-hint required></v-text-field>
							</v-col>
							<v-col cols="12">
								<v-text-field label="Email*" required></v-text-field>
							</v-col>
							<v-col cols="12">
								<v-text-field label="Password*" type="password" required></v-text-field>
							</v-col>
							<v-col cols="12" sm="6">
								<v-select :items="['0-17', '18-29', '30-54', '54+']" label="Age*" required></v-select>
							</v-col>
							<v-col cols="12" sm="6">
								<v-autocomplete
									:items="['Skiing', 'Ice hockey', 'Soccer', 'Basketball', 'Hockey', 'Reading', 'Writing', 'Coding', 'Basejump']"
									label="Interests" multiple></v-autocomplete>
							</v-col>
						</v-row>
					</v-container>
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn color="red" variant="text" @click="dialog_update = false">
						Disagree
					</v-btn>
					<v-btn color="green-darken-1" variant="text" @click="dialog_update = false">
						Agree
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>

		<!-- 刪除專案 -->
		<v-dialog v-model="dialog_delete" width="auto" persistent>
			<v-card>
				<v-card-text>
					你確定要刪除 專案 ?
				</v-card-text>
				<v-card-actions>
					<v-spacer></v-spacer>
					<v-btn color="red" variant="text" @click="dialog_delete = false">
						Disagree
					</v-btn>
					<v-btn color="green-darken-1" variant="text" @click="dialog_delete = false">
						Agree
					</v-btn>
				</v-card-actions>
			</v-card>
		</v-dialog>
	</main>
</template>

<script>
import axios from 'axios';
import { mapState, mapActions } from 'pinia'
import UserStatus from '@/stores/UserStatus'
import AppWrapper from '../components/AppWrapper.vue';

export default {
	data: () => ({
		// drawer: null,
		color_picker: null,
		dialog_create: false,
		dialog_delete: false,
		dialog_update: false,
		Project: [],
	}),
	components: {
		AppWrapper
	},
	computed: {
		...mapState(UserStatus, ['User'])
	},
	methods: {
		getProject() {
			let self = this;
			axios.get('http://127.0.0.1:5001/project')
			.then(function (response) {
				console.log(response);
				self.Project = response.data.Project;
			})
			.catch(function (error) {
				console.log(error);
			})
			.finally(function () {
			});
		}
	},
	mounted() {
		this.getProject();
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