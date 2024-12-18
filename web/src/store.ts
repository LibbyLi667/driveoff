import { reactive } from 'vue';
import { DataClassification, makeProject, type Project } from './project';

interface FormStateStore {
    hasStartedForm: boolean;
    hasFinishedForm: boolean;
    isCorrectDrive: boolean | null;
    areProjectDetailsCorrect: boolean | null;
    project: Project;
    dataClassification: DataClassification | null;
    retentionPeriod: number | null;
    isRetentionPeriodCustom: boolean | null;
}

export const formState: FormStateStore = reactive({
    hasStartedForm: false,
    hasFinishedForm: false,
    isCorrectDrive: null,
    areProjectDetailsCorrect: null,
    project: makeProject(),
    dataClassification: null,
    isRetentionPeriodCustom: null,
    retentionPeriod: null
});