export const validateName = (value: string) =>
  validateCredentials(
    {
      minLength: {
        condition: 2,
        message: "Минимальная длина - 2 символа",
      },
      maxLength: {
        condition: 25,
        message: "Максимальная длина - 25 символов",
      },
      pattern: {
        condition: /^[а-я А-ЯёЁ-]+$/,
        message: 'Поле может содержать только русские буквы или "-"',
      },
    },
    value
  );
  
export const validateMiddleName = (value: string) =>
  validateCredentials(
    {
      minLength: {
        condition: 2,
        message: "Минимальная длина - 2 символа",
      },
      maxLength: {
        condition: 25,
        message: "Максимальная длина - 25 символов",
      },
      pattern: {
        condition: /^[а-я А-ЯёЁ-]+$/,
        message: 'Поле может содержать только русские буквы или "-"',
      },
    },
    value
  );
export const validateLastName = (value: string) =>
  validateCredentials(
    {
      minLength: {
        condition: 2,
        message: "Минимальная длина - 2 символа",
      },
      maxLength: {
        condition: 50,
        message: "Максимальная длина - 50 символов",
      },
      pattern: {
        condition: /^[а-я А-ЯёЁ-]+$/,
        message: 'Поле может содержать только русские буквы или "-"',
      },
    },
    value
  );
export const validateFullName = (value: string) =>
  validateCredentials(
    {
      minLength: {
        condition: 2,
        message: "Минимальная длина - 2 символа",
      },
      maxLength: {
        condition: 100,
        message: "Максимальная длина - 100 символов",
      },
      pattern: {
        condition: /^[а-я А-ЯёЁ-]+$/,
        message: 'Поле может содержать только русские буквы или "-"',
      },
    },
    value
  );

export const validateCredentials = (
  currentRuleset: {
    minLength: { condition: number; message: string };
    maxLength: { condition: number; message: string };
    pattern: { condition: RegExp; message: string };
  },
  value: string
) => {
  switch (true) {
    case String(value).length < currentRuleset.minLength.condition:
      return currentRuleset.minLength.message;

    case String(value).length > currentRuleset.maxLength.condition:
      return currentRuleset.maxLength.message;

    case !String(value).match(currentRuleset.pattern.condition):
      return currentRuleset.pattern.message;

    default:
      return "";
  }
};

export const validateEmail = (value: string) => {
  const pattern = {
    condition: /^[\w-.]{1,50}@([\w-]+\.)+[\w-]{1,10}$/,
    message: "Некорректно введен E-mail",
  };

  if (!String(value).match(pattern.condition)) {
    return pattern.message;
  }
  return "";
};

export const validatePassword = (value: string) => {
  const minLength = {
    condition: 8,
    message: "Минимальная длина - 8 символов",
  };
  const patternCapitals = {
    condition: /[A-Z]/,
    message: "Пароль должен содержать хотя бы одну заглавную букву",
  };
  const patternLetters = {
    condition: /[a-z]/,
    message: "Пароль должен содержать хотя бы одну прописную букву",
  };
  const patternNumbers = {
    condition: /[0-9]/,
    message: "Пароль должен содержать хотя бы одну цифру",
  };
  const patternRussian = {
    condition: /^[^а-яА-ЯеЁ]+$/,
    message: "Пароль не должен содержать русские буквы",
  };
  const patternSpace = {
    condition: /^\S+$/,
    message: "Пароль не должен содержать пробелы",
  };

  switch (true) {
    case String(value).length < minLength.condition:
      return minLength.message;

    case !String(value).match(patternRussian.condition):
      return patternRussian.message;

    case !String(value).match(patternCapitals.condition):
      return patternCapitals.message;

    case !String(value).match(patternLetters.condition):
      return patternLetters.message;

    case !String(value).match(patternNumbers.condition):
      return patternNumbers.message;

    case !String(value).match(patternSpace.condition):
      return patternSpace.message;

    default:
      return "";
  }
};

export const validateTextarea = (value: string) => {
  const maxLength = {
    condition: 1200,
    message: "Максимальная длина - 1200 символов",
  };
  const pattern = {
    condition: /^[\wа-яА-ЯёЁ\d.,?!:;()%№@+="\s-]+$/,
    message:
      'Поле может содержать русские/латинские буквы и символы "-.,?!-:;()%№@+="',
  };

  switch (true) {
    case String(value).length === 0:
      return "Поле не может быть пустым";
      
    case String(value).length > maxLength.condition:
      return maxLength.message;

    case !String(value).match(pattern.condition):
      return pattern.message;

    case String(value).trim() === "":
      return "Поле не может быть пустым";

    default:
      return "";
  }
};

export const validateOrderNumber = (value: string) => {
  const pattern = {
    condition: /^[\wа-яА-ЯёЁ]+$/,
    message: "Поле может содержать только русские/латинские буквы и цифры",
  };

  if (!String(value).match(pattern.condition)) {
    return pattern.message;
  }
  return "";
};

export const validateUrl = () => {
  return "";
};

export const validateCardNumber = (value: string) => {
  const maxLength = {
    condition: 20,
    message: "Максимальная длина - 20 символов",
  };
  const pattern = {
    condition: /^[0-9]+$/,
    message: "Поле может содержать только цифры",
  };

  switch (true) {
    case String(value).length > maxLength.condition:
      return maxLength.message;

    case !String(value).match(pattern.condition):
      return pattern.message;

    default:
      return "";
  }
};

export const validateComment = (value: string) => {
  const maxLength = {
    condition: 600,
    message: "Максимальная длина - 600 символов",
  };
  const pattern = {
    condition: /^[\wа-яА-ЯёЁ\d.,?!:;()%№@+="\s-]+$/,
    message:
      'Поле может содержать только русские/латинские буквы и символы "-.,?!-:;()%№@+="',
  };

  switch (true) {
    case String(value).length > maxLength.condition:
      return maxLength.message;

    case !String(value).match(pattern.condition):
      return pattern.message;

    default:
      return "";
  }
};

export const validatePhoneNumber = (value: string) => {
  value = String(value).replace(/[^0-9]/g, "");

  const length = {
    condition: 11,
    message: "Некорректно введен номер телефона",
  };

  if (String(value).length !== length.condition) {
    return length.message;
  }

  return "";
};

export const validateConfirmPassword = (
  value: string,
  checkAgainstValue: string
) => {
  if (value === checkAgainstValue) {
    return "";
  }
  return "Пароли не совпадают";
};

export const validateBirthday = (value: string) => {
  const inputDate = String(value).split("-");
  const inputYear = +inputDate[0];
  const inputMonth = +inputDate[1];
  const inputDay = +inputDate[2];

  const currentYear = new Date().getFullYear();

  const maxDay = {
    condition: 31,
    message: "Некорректно введен день",
  };
  const maxMonth = {
    condition: 12,
    message: "Некорректно введен месяц",
  };
  const year = {
    maxDelta: 100,
    message: "Некорректно введен год",
  };

  switch (true) {
    case inputDay > maxDay.condition || inputDay < 1:
      return maxDay.message;

    case inputMonth > maxMonth.condition || inputMonth < 1:
      return maxMonth.message;

    case inputYear - currentYear > year.maxDelta || inputYear > currentYear:
      return year.message;

    default:
      return "";
  }
};

export const validateAddress = (value: string) => {
  const currentRuleset = {
    pattern: {
      condition: /^[а-яА-ЯёЁ\d[&+,:;=?@#|'<>"^*()%!-_\s]+$/,
      message: "Поле содержит недопустимые символы",
    },
  };

  if (!String(value).match(currentRuleset.pattern.condition)) {
    return currentRuleset.pattern.message;
  }
  return "";
};

export type TFormData = {
  [key: string]: {
    value: any;
    error: string;
    required: boolean;
  };
};

export const validateForm = (formData: TFormData): boolean => {
  let error = false;

  for (const key in formData) {
    if (formData[key].required) {
      if (key === "phone") {
        formData[key].error = validatePhoneNumber(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "email") {
        formData[key].error = validateEmail(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "name") {
        formData[key].error = validateName(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "captcha") {
        formData[key].error = formData[key].value
          ? ""
          : "Необходимо пройти антиспам проверку";
        if (formData[key].error) {
          error = true;
        }
      } else if (key === "comment") {
        formData[key].error = validateTextarea(formData[key].value);
        if (formData[key].error) {
          error = true;
        }
      } else {
        formData[key].error = formData[key].value
          ? ""
          : "Поле необходимо к заполнению";
        if (formData[key].error) {
          error = true;
        }
      }
    }
  }
  return error;
};
