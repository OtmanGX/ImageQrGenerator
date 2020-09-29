async function ajaxDownloadCounter(id) {
    console.log(id);
    $.ajax({
        url: `/image/download/${id}`,
        success: async function (data) {
            console.log(data);
        }
    });
};
async function ajaxContactCounter(id) {
    console.log(id);
    $.ajax({
        url: `/image/contact/${id}`,
        success: async function (data) {
            console.log(data);
        }
    });
};