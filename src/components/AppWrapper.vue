<template>
    <v-app id="inspire">
        <v-app-bar>
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title>
                ProjectMgnt
            </v-toolbar-title>
            <v-btn class="bg-black" @click="logout()">登出</v-btn>
        </v-app-bar>

        <!-- https://vuetifyjs.com/en/components/navigation-drawers/#location -->
        <v-navigation-drawer v-model="drawer">
            <template v-slot:prepend>
                <v-list-item lines="two" :prepend-avatar="this.User.User_Avatar"
                    :title="this.User.User_Name" :subtitle="this.User.User_Mail"></v-list-item>
            </template>

            <v-divider></v-divider>

            <v-list density="compact" nav>
                <v-list-item to="/home" prepend-icon="mdi-home-city" title="Home" value="home"></v-list-item>
                <!-- <v-list-item prepend-icon="mdi-account" title="My Account" value="account"></v-list-item> -->
                <!-- <v-list-item prepend-icon="mdi-account-group-outline" title="WorksOn" value="WorksOn"></v-list-item> -->
            </v-list>
        </v-navigation-drawer>
        <v-main class="bg-grey-lighten-2">
            <slot></slot>
        </v-main>
    </v-app>
</template>

<script>
import axios from 'axios';
import { mapState, mapActions } from 'pinia'
import UserStatus from '@/stores/UserStatus'

export default {
    data: () => ({
        drawer: false,
    }),
    computed: {
		...mapState(UserStatus, ['User'])
	},
	methods: {
		...mapActions(UserStatus, ['checkAuth', 'logout']),
    },
    mounted() {
        (async () => {
			await this.checkAuth();
		})();
    }
}
</script>