export const phoneUtils = {
  validate(event: InputEvent & { target: HTMLInputElement }) {
    const caretPosition = this.getCaretPosition(event);
    const value = this.getPhoneValue(event);
    event.target.value = this.formatedPhoneInput(value);
    this.setCaretPosition(event, caretPosition);
  },

  getCaretPosition(event): number {
    const position = event.target.selectionStart;
    const isDeleting =
      event.inputType === 'deleteContentBackward' ||
      event.inputType === 'deleteContentForward';

    if (position < 4) {
      return isDeleting ? 3 : 4;
    }
    if (position > 6 && position < 8) {
      return isDeleting ? 6 : 8;
    }
    if (position === 11) {
      return isDeleting ? 10 : 12;
    }
    if (position === 14) {
      return isDeleting ? 13 : 15;
    }
    return position;
  },
  getPhoneValue(event) {
    if (event.target.value.length === 11 && event.target.value[0] === '8') {
      event.target.value = event.target.value.slice(1);
    }

    let value = event.target.value.replace(/(\+7)|\D/g, '');

    if (value.length >= 10) {
      event.target.value = event.target.value.slice(0, 17);
      value = value.slice(0, 10);
    }

    return value;
  },
  formatedPhoneInput(value: string) {
    if (value.startsWith('7') || value.startsWith('8')) {
      value = '';
      return '+7 ';
    }

    const match = value.match(/^(\d{1,3})(\d{0,3})(\d{0,2})(\d{0,2})$/);
    if (match) {
      return `+7 ${match[1]}${match[2] ? ' ' : ''}${match[2]}${
        match[3] ? ' ' : ''
      }${match[3]}${match[4] ? ' ' : ''}${match[4]}`;
    } else {
      return '';
    }
  },
  setCaretPosition(event, position: number) {
    event.target.selectionStart = position;
    event.target.selectionEnd = position;
  },
};
