$(document).ready(function () {
    $(document).on('click', '.qtybtn', function () {
        let quantity = $(this).parent('.pro-qty-2').find('.quantityVal').val()
        let cartId = $(this).parent('.pro-qty-2').parent('.quantity').find('.cartId').val()

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({'quantity': quantity, 'id': cartId})
        })
            .then((res) => {
                window.location.reload()

            })
            .catch(err => console.log(err))
    })
});