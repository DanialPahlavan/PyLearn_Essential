# Store Management System Enhancements README

Welcome to the updated Store Management System! This README outlines the new features and functionalities added to enhance your experience with the system.

## New Features

- **Edit Product Information**: Users can now update product details by entering the product code and selecting the field they wish to edit:
  1. Name
  2. Price
  3. Count
  After entering the new value, the system will confirm the successful update with a message.

- **Delete Product**: Users can remove a product from the inventory by providing its code. A confirmation message will be displayed upon successful deletion.

- **QR Code Generation**: The system now includes a function that takes a product code and saves the product information as a QR Code.

- **Shopping Process**:
  a) The system prompts for the product code. If the product does not exist, an appropriate message is displayed.
  b) If the product exists, the system asks for the quantity the user wishes to purchase.
  c) If there is insufficient stock, a message is displayed. Otherwise, the quantity is deducted from the inventory and added to the user's cart.
  d) The shopping process continues until the user decides to stop adding new products (using a `while` loop).
  e) Upon completion of shopping, an invoice is printed, including the price of each product and the total amount.

- **Save Information on Exit**: When exiting the program, all information is saved to a file for future reference.

## How to Use

1. Start the system and follow the prompts to manage products or shop.
2. To edit or delete a product, enter the product code and follow the instructions.
3. To shop, enter the product codes and quantities as prompted.
4. Before exiting, ensure all transactions are complete to save the information correctly.

## Contributing

Feel free to contribute to the system by submitting pull requests with your ideas or improvements.

## Support

If you encounter any issues or have questions, please open an issue, and we'll assist you as soon as possible.

Enjoy the enhanced Store Management System!
