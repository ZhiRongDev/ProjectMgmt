<script setup>
</script>

<template>
	<main>
		<v-app id="inspire">
			<v-app-bar>
				<v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

				<v-toolbar-title>Application</v-toolbar-title>
			</v-app-bar>

			<v-navigation-drawer v-model="drawer" temporary>
				<!--  -->
			</v-navigation-drawer>

			<v-main class="bg-grey-lighten-2">
				<v-container>
					<v-row>
						<template v-for="n in 1" :key="n">
							<v-col class="mt-2" cols="12">
								<h2>專案</h2>
							</v-col>

							<v-col v-for="(item, j) in project" :key="`${n}${j}`" cols="12" sm="6" md="4">
								<!-- <v-sheet height="150"></v-sheet> -->
								<div>
									<v-hover v-slot="{ isHovering, props }">
										<v-card class="mx-auto" height="200" v-bind="props">
											<!-- <v-img src="https://cdn.vuetifyjs.com/images/cards/forest-art.jpg"></v-img> -->

											<v-card-text class="d-flex justify-center align-center h-100">
												<h2 class="text-h6 text-primary">
													{{ item }}
												</h2>
											</v-card-text>

											<v-overlay :model-value="isHovering" contained scrim="#036358"
												class="align-center justify-center">
												<v-row>
													<v-col>
														<v-btn variant="flat" color="primary">進入</v-btn>
													</v-col>
													<v-col>
														<v-btn variant="flat" color="secondary"
															@click="dialog_update = true">更改</v-btn>
													</v-col>
													<v-col>
														<v-btn variant="flat" color="red"
															@click="dialog_delete = true">刪除</v-btn>
													</v-col>
												</v-row>
											</v-overlay>
										</v-card>
									</v-hover>
								</div>
							</v-col>
						</template>
					</v-row>
				</v-container>
			</v-main>
		</v-app>

		<!-- 更改 -->
		<v-dialog v-model="dialog_update" width="auto" persistent>
			<v-card>
				<v-card-text>
					<v-container>
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

		<!-- 刪除 -->
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
export default {
	data: () => ({
		drawer: null,
		dialog_delete: false,
		dialog_update: false,
		project: ["專案 1", "專案 2"]
	}),
}
</script>