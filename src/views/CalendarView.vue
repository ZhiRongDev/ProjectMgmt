<!-- https://fullcalendar.io/docs/vue -->

<template>
    <div>

    </div>
</template>

<script>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import interactionPlugin from '@fullcalendar/interaction'

export default {
    data() {
        return {
            calendarOptions: {
                plugins: [dayGridPlugin, interactionPlugin],
                initialView: 'dayGridMonth',
                dateClick: this.handleDateClick,
                events: [
                    { title: 'event 1', date: '2023-05-01' },
                    { title: 'event 2', date: '2023-05-02' }
                ]
            },
        }
    },
    components: {
        FullCalendar
    },
    methods: {
        handleDateClick(arg) {
            alert('date click! ' + arg.dateStr);
        },
    }
}

</script>