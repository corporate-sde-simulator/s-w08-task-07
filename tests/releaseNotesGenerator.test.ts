import { ReleaseNotesGenerator } from "../src/releaseNotesGenerator";
import { CommitParser } from "../src/commitParser";

describe("Release notes auto-generator", () => {
    test("should process valid input", () => {
        const obj = new ReleaseNotesGenerator();
        expect(obj.process({ key: "val" })).not.toBeNull();
    });
    test("should handle null", () => {
        const obj = new ReleaseNotesGenerator();
        expect(obj.process(null)).toBeNull();
    });
    test("should track stats", () => {
        const obj = new ReleaseNotesGenerator();
        obj.process({ x: 1 });
        expect(obj.getStats().processed).toBe(1);
    });
    test("support should work", () => {
        const obj = new CommitParser();
        expect(obj.process({ data: "test" })).not.toBeNull();
    });
});
