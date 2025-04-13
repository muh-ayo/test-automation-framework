class Locators:
    USERNAME_FIELD = "//input[@placeholder='Username']"
    PASSWORD_FIELD = "//input[@placeholder='Password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    ERROR_MESSAGE_FIELD = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
    MENU_BUTTON = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    LOGOUT_BUTTON = "//a[normalize-space()='Logout']"
    EMPTY_ERROR_FIELD = "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    DASH_TEXT_FIELD = "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']"
