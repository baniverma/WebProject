document.addEventListener("DOMContentLoaded", () => {
    const drinkCards = document.querySelectorAll(".drink-card");
    const cartContainer = document.getElementById("cart");
    const checkoutButton = document.getElementById("checkoutButton");
    const orderSummaryBox = document.getElementById("orderSummaryBox");
    const closeOrderSummary = document.getElementById("closeOrderSummary");
    const orderSummaryContent = document.getElementById("orderSummaryContent");

    let cart = [];

    function updateCart() {
        cartContainer.innerHTML = "";
        if (cart.length === 0) {
            cartContainer.innerHTML = "<p>Your cart is empty.</p>";
        } else {
            cart.forEach((item, index) => {
                const div = document.createElement("div");
                div.innerHTML = `
                    <p>${item.name} - $${item.price.toFixed(2)} x ${item.quantity}</p>
                    <button class="decrease" data-index="${index}">-</button>
                    <button class="increase" data-index="${index}">+</button>
                    <button class="remove" data-index="${index}">Remove</button>
                `;
                cartContainer.appendChild(div);
            });
        }
    }

    drinkCards.forEach(card => {
        card.addEventListener("click", () => {
            const name = card.dataset.name;
            const price = parseFloat(card.dataset.price);
            const existingItem = cart.find(item => item.name === name);
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({ name, price, quantity: 1 });
            }
            updateCart();
        });
    });

    cartContainer.addEventListener("click", e => {
        const index = e.target.dataset.index;
        if (e.target.classList.contains("increase")) {
            cart[index].quantity += 1;
        } else if (e.target.classList.contains("decrease")) {
            if (cart[index].quantity > 1) {
                cart[index].quantity -= 1;
            } else {
                cart.splice(index, 1);
            }
        } else if (e.target.classList.contains("remove")) {
            cart.splice(index, 1);
        }
        updateCart();
    });

    checkoutButton.addEventListener("click", () => {
        if (cart.length === 0) {
            alert("Your cart is empty.");
            return;
        }
        let total = 0;
        let summary = "Order Summary:\n\n";
        cart.forEach(item => {
            const itemTotal = item.price * item.quantity;
            summary += `${item.name} - $${item.price.toFixed(2)} x ${item.quantity} = $${itemTotal.toFixed(2)}\n`;
            total += itemTotal;
        });
        summary += `\nTotal: $${total.toFixed(2)}`;
        orderSummaryContent.textContent = summary;
        orderSummaryBox.style.display = "block";
    });

    closeOrderSummary.addEventListener("click", () => {
        orderSummaryBox.style.display = "none";
    });
});
